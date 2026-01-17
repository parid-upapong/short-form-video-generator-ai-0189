import React from 'react';
import { STRATEGIC_CONFIG } from '../constants/vision';

const HeroSection: React.FC = () => {
  return (
    <div className="hero-container" style={{ backgroundColor: '#000', color: '#fff', padding: '100px 20px' }}>
      <header>
        <h1 style={{ fontSize: '4rem', fontWeight: 'bold' }}>
          From Long-form to <span style={{ color: STRATEGIC_CONFIG.BRAND_TONE.PRIMARY_COLOR }}>Viral</span> in Minutes.
        </h1>
        <p style={{ fontSize: '1.5rem', maxWidth: '800px', margin: '20px auto' }}>
          {STRATEGIC_CONFIG.MISSION} No editing skills required. Let our AI find your best moments 
          and turn them into high-performing TikToks and Reels.
        </p>
        <div className="cta-group" style={{ marginTop: '40px' }}>
          <button style={{ 
            padding: '15px 40px', 
            fontSize: '1.2rem', 
            borderRadius: '30px', 
            border: 'none', 
            background: `linear-gradient(90deg, ${STRATEGIC_CONFIG.BRAND_TONE.PRIMARY_COLOR}, ${STRATEGIC_CONFIG.BRAND_TONE.SECONDARY_COLOR})`,
            color: '#fff',
            cursor: 'pointer'
          }}>
            Start Your Viral Journey
          </button>
        </div>
      </header>
      
      <div className="stats-bar" style={{ display: 'flex', justifyContent: 'center', gap: '50px', marginTop: '60px' }}>
        <div>
          <h3>{STRATEGIC_CONFIG.KPI_TARGETS.REDUCTION_IN_EDITING_TIME_PERCENT}%</h3>
          <p>Faster Editing</p>
        </div>
        <div>
          <h3>Zero</h3>
          <p>Editing Skills Needed</p>
        </div>
        <div>
          <h3>AI-Powered</h3>
          <p>Virality Prediction</p>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;