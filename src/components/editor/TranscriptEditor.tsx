'use client';

import React from 'react';
import { TranscriptSegment } from '@/types/project';
import { Wand2 } from 'lucide-react';

interface TranscriptEditorProps {
  segments: TranscriptSegment[];
  currentTime: number;
  onSegmentUpdate: (id: string, newText: string) => void;
}

export const TranscriptEditor: React.FC<TranscriptEditorProps> = ({ 
  segments, 
  currentTime, 
  onSegmentUpdate 
}) => {
  return (
    <div className="flex flex-col h-full bg-zinc-900 border-l border-zinc-800">
      <div className="p-4 border-b border-zinc-800 flex justify-between items-center">
        <h3 className="font-semibold text-zinc-200">AI Transcript</h3>
        <button className="flex items-center gap-2 text-xs bg-zinc-800 hover:bg-zinc-700 px-3 py-1.5 rounded-lg transition">
          <Wand2 size={14} className="text-purple-400" />
          Regenerate
        </button>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {segments.map((segment) => {
          const isActive = currentTime >= segment.start && currentTime <= segment.end;
          return (
            <div 
              key={segment.id}
              className={`p-3 rounded-lg transition-all border ${
                isActive 
                ? 'bg-purple-500/10 border-purple-500/50' 
                : 'bg-transparent border-transparent hover:border-zinc-700'
              }`}
            >
              <div className="flex justify-between text-[10px] text-zinc-500 mb-1">
                <span>{segment.speaker || 'Speaker 1'}</span>
                <span>{segment.start.toFixed(2)}s</span>
              </div>
              <textarea
                value={segment.text}
                onChange={(e) => onSegmentUpdate(segment.id, e.target.value)}
                className="w-full bg-transparent text-sm text-zinc-300 focus:outline-none resize-none leading-relaxed"
                rows={2}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};