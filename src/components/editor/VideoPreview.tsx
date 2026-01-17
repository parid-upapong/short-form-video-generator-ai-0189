'use client';

import React, { useRef, useState, useEffect } from 'react';
import { Play, Pause, Maximize, Volume2 } from 'lucide-react';

interface VideoPreviewProps {
  url: string;
  currentTime: number;
  onTimeUpdate: (time: number) => void;
}

export const VideoPreview: React.FC<VideoPreviewProps> = ({ url, currentTime, onTimeUpdate }) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const togglePlay = () => {
    if (videoRef.current) {
      if (isPlaying) videoRef.current.pause();
      else videoRef.current.play();
      setIsPlaying(!isPlaying);
    }
  };

  return (
    <div className="relative group bg-black rounded-xl overflow-hidden shadow-2xl aspect-[9/16] max-h-[70vh] mx-auto">
      <video
        ref={videoRef}
        src={url}
        className="w-full h-full object-contain"
        onTimeUpdate={(e) => onTimeUpdate(e.currentTarget.currentTime)}
      />
      
      {/* Overlay Controls */}
      <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity">
        <div className="flex items-center gap-4">
          <button onClick={togglePlay} className="text-white hover:scale-110 transition">
            {isPlaying ? <Pause size={24} fill="white" /> : <Play size={24} fill="white" />}
          </button>
          <div className="flex-1 h-1 bg-white/30 rounded-full overflow-hidden">
            <div 
              className="h-full bg-purple-500" 
              style={{ width: `${(currentTime / (videoRef.current?.duration || 1)) * 100}%` }}
            />
          </div>
          <Volume2 size={20} className="text-white" />
        </div>
      </div>

      {/* AI Smart Crop Badge */}
      <div className="absolute top-4 left-4">
        <span className="bg-purple-600/90 text-[10px] font-bold px-2 py-1 rounded-md text-white uppercase tracking-wider backdrop-blur-sm">
          AI Smart Crop Active
        </span>
      </div>
    </div>
  );
};