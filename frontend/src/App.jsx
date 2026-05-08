import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [stats, setStats] = useState({ total_gardens: 0, active_alerts: 0, auto_tasks: 0 });

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/community-stats/')
      .then(res => setStats(res.data))
      .catch(() => {
        // Removed 'err' since we weren't using it
        console.log("Backend not running yet or connection refused");
      });
  }, []);

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif', backgroundColor: '#f4f7f6', minHeight: '100vh' }}>
      <h1 style={{ color: '#2d5a27' }}>Smart Uturima Dashboard</h1>
      <p>IDA Technology Internship Project - Community Solution</p>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginTop: '30px' }}>
        <div style={cardStyle("#fff", "4px solid #4caf50")}>
          <h3>Active Gardens</h3>
          <p style={{ fontSize: '2rem', fontWeight: 'bold' }}>{stats.total_gardens}</p>
        </div>
        <div style={cardStyle("#fff", "4px solid #f44336")}>
          <h3>Pending Alerts</h3>
          <p style={{ fontSize: '2rem', fontWeight: 'bold', color: '#f44336' }}>{stats.active_alerts}</p>
        </div>
        <div style={cardStyle("#fff", "4px solid #2196f3")}>
          <h3>AI Automated Tasks</h3>
          <p style={{ fontSize: '2rem', fontWeight: 'bold' }}>{stats.auto_tasks}</p>
        </div>
      </div>
    </div>
  );
}

const cardStyle = (bg, border) => ({
  background: bg,
  padding: '20px',
  borderRadius: '8px',
  boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
  borderTop: border
});

export default App;