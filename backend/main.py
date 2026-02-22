import csv
from io import StringIO
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

# Generate database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Glide Diagnostic Engine API")

@app.get("/")
def read_root():
    return {"status": "operational", "message": "Glide engine is ready."}

@app.post("/events", response_model=schemas.TaskEventResponse)
def create_event(event: schemas.TaskEventCreate, db: Session = Depends(get_db)):
    db_event = models.TaskEvent(
        task_id=event.task_id,
        previous_status=event.previous_status,
        new_status=event.new_status,
        assigned_to=event.assigned_to
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.get("/events", response_model=list[schemas.TaskEventResponse])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = db.query(models.TaskEvent).offset(skip).limit(limit).all()
    return events

@app.post("/upload-csv/")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = file.file.read()
    buffer = StringIO(contents.decode('utf-8'))
    csvReader = csv.DictReader(buffer)
    
    events = []
    for row in csvReader:
        db_event = models.TaskEvent(
            task_id=row.get('task_id'),
            previous_status=row.get('previous_status'),
            new_status=row.get('new_status'),
            assigned_to=row.get('assigned_to')
        )
        events.append(db_event)
        
    db.bulk_save_objects(events)
    db.commit()
    return {"filename": file.filename, "records_inserted": len(events)}