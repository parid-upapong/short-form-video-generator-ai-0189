export interface HighlightClip {
  id: string;
  startTime: number;
  endTime: number;
  viralScore: number;
  justification: string;
  transcript: TranscriptSegment[];
  thumbnailUrl: string;
  videoUrl: string;
  aspectRatio: '9:16' | '1:1' | 'original';
}

export interface TranscriptSegment {
  id: string;
  text: string;
  start: number;
  end: number;
  speaker?: string;
}

export interface Project {
  id: string;
  title: string;
  originalVideoUrl: string;
  status: 'processing' | 'completed' | 'failed';
  highlights: HighlightClip[];
}