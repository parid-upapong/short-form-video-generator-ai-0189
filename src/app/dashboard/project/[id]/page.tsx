'use client';

import React, { useState } from 'react';
import { VideoPreview } from '@/components/editor/VideoPreview';
import { TranscriptEditor } from '@/components/editor/TranscriptEditor';
import { 
  Layers, 
  Type, 
  Scissors, 
  Share2, 
  Download,
  ChevronLeft,
  Sparkles
} from 'lucide-react';

export default function QuickEditDashboard({ params }: { params: { id: string } }) {
  const [currentTime, setCurrentTime] = useState(0);
  
  // Mock Data (In production, fetch via React Query using params.id)
  const [mockClip] = useState({
    id: 'clip-101',
    videoUrl: 'https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
    viralScore: 94,
    justification: "Strong emotional hook identified in the first 5 seconds.",
    transcript: [
      { id: '1', start: 0, end: 3.5, text: "Wait, you actually think that AI is going to replace developers?" },
      { id: '2', start: 3.6, end: 7.2, text: "Let me tell you why you're looking at this the wrong way." },
    ]
  });

  return (
    <div className="flex flex-col h-screen bg-black text-white overflow-hidden">
      {/* Top Header */}
      <header className="h-14 border-b border-zinc-800 flex items-center justify-between px-4 bg-zinc-950">
        <div className="flex items-center gap-4">
          <button className="p-2 hover:bg-zinc-800 rounded-full">
            <ChevronLeft size={20} />
          </button>
          <h1 className="font-medium text-sm">Project: AI Revolution Podcast</h1>
          <div className="flex items-center gap-2 bg-purple-500/20 px-2 py-0.5 rounded border border-purple-500/30">
            <Sparkles size={12} className="text-purple-400" />
            <span className="text-[10px] text-purple-300 font-bold uppercase tracking-tighter">
              Score: {mockClip.viralScore}/100
            </span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button className="flex items-center gap-2 bg-zinc-800 hover:bg-zinc-700 px-4 py-1.5 rounded-lg text-sm transition">
            <Share2 size={16} /> Share
          </button>
          <button className="flex items-center gap-2 bg-purple-600 hover:bg-purple-500 px-4 py-1.5 rounded-lg text-sm font-semibold transition shadow-lg shadow-purple-500/20">
            <Download size={16} /> Export Clip
          </button>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex flex-1 overflow-hidden">
        {/* Left Toolbar */}
        <aside className="w-16 border-r border-zinc-800 flex flex-col items-center py-6 gap-8 bg-zinc-950">
          <button className="p-3 text-purple-500 bg-purple-500/10 rounded-xl" title="Layout">
            <Layers size={22} />
          </button>
          <button className="p-3 text-zinc-400 hover:text-white transition" title="Captions">
            <Type size={22} />
          </button>
          <button className="p-3 text-zinc-400 hover:text-white transition" title="Trim">
            <Scissors size={22} />
          </button>
        </aside>

        {/* Center: Video Stage */}
        <section className="flex-1 flex flex-col bg-zinc-900/50 relative p-8 overflow-y-auto">
          <div className="flex-1 flex items-center justify-center">
            <VideoPreview 
              url={mockClip.videoUrl} 
              currentTime={currentTime} 
              onTimeUpdate={setCurrentTime}
            />
          </div>
          
          {/* AI Justification Card */}
          <div className="mt-8 mx-auto max-w-2xl bg-zinc-900 border border-zinc-800 p-4 rounded-xl">
            <h4 className="text-xs font-bold text-zinc-500 uppercase mb-2 flex items-center gap-2">
              <Sparkles size={12} /> Why this is viral:
            </h4>
            <p className="text-sm text-zinc-300 italic">"{mockClip.justification}"</p>
          </div>
        </section>

        {/* Right: Transcription Panel */}
        <aside className="w-80 border-l border-zinc-800">
          <TranscriptEditor 
            segments={mockClip.transcript} 
            currentTime={currentTime}
            onSegmentUpdate={(id, text) => console.log('Update', id, text)}
          />
        </aside>
      </main>

      {/* Mini Timeline Footer */}
      <footer className="h-20 bg-zinc-950 border-t border-zinc-800 flex items-center px-6">
        <div className="w-full h-12 bg-zinc-900 rounded-lg relative overflow-hidden border border-zinc-800">
           {/* Visual waveform placeholder */}
           <div className="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/graphy.png')]" />
           <div className="absolute top-0 bottom-0 w-1 bg-purple-500 z-10" style={{ left: '30%' }} />
           <div className="absolute top-0 bottom-0 left-[20%] right-[40%] bg-purple-500/20 border-x border-purple-500/50" />
        </div>
      </footer>
    </div>
  );
}