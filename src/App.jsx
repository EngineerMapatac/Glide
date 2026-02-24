import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-black text-white font-sans selection:bg-gray-800">
      <nav className="flex justify-center py-6 text-sm font-medium tracking-wide text-gray-400">
        <ul className="flex space-x-12">
          <li className="text-white cursor-pointer">Glide.</li>
          <li className="hover:text-white cursor-pointer transition-colors">Engine</li>
          <li className="hover:text-white cursor-pointer transition-colors">Metrics</li>
          <li className="hover:text-white cursor-pointer transition-colors">GitHub</li>
        </ul>
      </nav>

      <main className="flex flex-col items-center justify-center min-h-[80vh] px-6 text-center">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="text-6xl md:text-8xl font-semibold tracking-tighter mb-6"
        >
          Process,<br />perfected.
        </motion.h1>
        
        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.3 }}
          className="text-xl md:text-2xl text-gray-400 max-w-2xl font-light tracking-wide mb-12"
        >
          An automated diagnostic engine to cut process waste, spot bottlenecks, and keep workflows moving.
        </motion.p>

        <motion.button 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.6 }}
          className="flex items-center space-x-2 bg-white text-black px-8 py-4 rounded-full font-medium text-lg hover:bg-gray-200 transition-colors"
        >
          <span>Deploy Engine</span>
          <ArrowRight size={20} />
        </motion.button>
      </main>
    </div>
  );
}