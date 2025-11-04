import React, { useState } from 'react';
import {
  Box,
  TextField,
  Button,
  Paper,
  Typography,
  Alert,
  CircularProgress,
} from '@mui/material';
import axios from 'axios';

interface ScanResult {
  is_phishing: boolean;
  confidence: number;
  message: string;
}

const EmailScanner: React.FC = () => {
  const [emailText, setEmailText] = useState('');
  const [result, setResult] = useState<ScanResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleScan = async () => {
    if (!emailText.trim()) {
      setError('Please enter email text');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/scan/', {
        email: emailText,
      });
      setResult(response.data);
    } catch (err) {
      setError('Failed to scan email. Please try again.');
      console.error('Error scanning email:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ maxWidth: 800, mx: 'auto', mt: 4, p: 2 }}>
      <Typography variant="h4" gutterBottom>
        PhishGuard Email Scanner
      </Typography>
      <Paper sx={{ p: 3, mb: 3 }}>
        <TextField
          fullWidth
          multiline
          rows={6}
          variant="outlined"
          label="Paste email content here"
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
          sx={{ mb: 2 }}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleScan}
          disabled={loading}
          fullWidth
        >
          {loading ? <CircularProgress size={24} /> : 'Scan Email'}
        </Button>
      </Paper>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {result && (
        <Paper sx={{ p: 3 }}>
          <Alert
            severity={result.is_phishing ? 'warning' : 'success'}
            sx={{ mb: 2 }}
          >
            {result.message}
          </Alert>
          <Typography variant="body1">
            Confidence: {(result.confidence * 100).toFixed(1)}%
          </Typography>
        </Paper>
      )}
    </Box>
  );
};

export default EmailScanner;