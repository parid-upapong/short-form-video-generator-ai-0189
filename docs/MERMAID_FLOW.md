graph TD
    %% Start of the flow
    Start((User Enters App)) --> Dashboard[Dashboard]
    
    %% Ingestion
    Dashboard --> Upload{Upload/Link Video}
    Upload -->|Paste URL| AI_Process[AI Analysis Engine]
    Upload -->|Upload File| AI_Process
    
    %% AI Processing
    subgraph AI Engine Logic
        AI_Process --> Transcribe[Transcription]
        AI_Process --> Saliency[Saliency/Hook Detection]
        AI_Process --> AutoCrop[Smart Face Cropping]
    end
    
    %% Review
    Saliency --> Results[Highlight Grid View]
    Results -->|User Selects Clip| Studio[Refine Studio]
    
    %% Refine
    subgraph Studio Features
        Studio --> CapStyles[Apply Caption Styles]
        Studio --> AdjustCrop[Manual Crop Adjustment]
        Studio --> Trim[Quick Trim]
    end
    
    %% Finalize
    Studio --> Export{Finalize}
    Export -->|Download| MP4[Video File]
    Export -->|Direct Share| TikTok[TikTok/Reels API]
    
    %% Feedback
    MP4 --> Feedback[AI Training Feedback]
    TikTok --> Feedback
    Feedback -.->|Refines Model| AI_Process