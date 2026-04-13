// transcript → DOM · escape HTML · render newlines as <br>
function renderChat() {
  document.getElementById('ai-messages').innerHTML = chatHistory.map(
    m => `<div class="ai-msg ${m.role}">`
      + m.content.replace(/</g, '&lt;').replace(/\n/g, '<br>')
      + `</div>`
  ).join('');
}
