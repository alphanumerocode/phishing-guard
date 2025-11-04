import React from 'react';
import { CssBaseline, Container, ThemeProvider, createTheme } from '@mui/material';
import EmailScanner from './components/EmailScanner';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container>
        <EmailScanner />
      </Container>
    </ThemeProvider>
  );
}

export default App;
