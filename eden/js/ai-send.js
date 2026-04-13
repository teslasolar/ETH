// POST to /v1/messages with current file as context
async function sendToAI(msg, action) {
  if (!currentFile?.content) return;

  const actionPrompts = {
    explain: 'Explain this code',
    refactor: 'Suggest improvements',
    bugs: 'Find bugs',
    run: 'How to run this?',
  };
  const prompt = msg || actionPrompts[action] || msg;

  chatHistory.push({ role: 'user', content: prompt });
  renderChat();
  document.getElementById('ai-status').textContent = '🤖 Thinking...';

  try {
    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 600,
        system: `Code assistant for: ${currentFile.path}\n\n`
          + currentFile.content.substring(0, 1200),
        messages: [{ role: 'user', content: prompt }],
      }),
    });
    const data = await res.json();
    chatHistory.push({
      role: 'assistant',
      content: data.content?.[0]?.text || 'Error',
    });
  } catch (e) {
    chatHistory.push({
      role: 'assistant',
      content: 'AI unavailable. Check the code tab.',
    });
  }

  renderChat();
  document.getElementById('ai-status').textContent = '🤖 Ready';
}
