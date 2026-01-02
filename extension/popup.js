const btn = document.getElementById("generate");
const output = document.getElementById("output");

btn.onclick = async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.tabs.sendMessage(tab.id, { type: "GET_VIDEO_ID" }, async (res) => {
    const url = `https://www.youtube.com/watch?v=${res.videoId}`;

    const response = await fetch("http://localhost:8000/transcript", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });

    const data = await response.json();
    output.textContent = data.segments
      .map((s) => `[${Math.floor(s.start)}s] ${s.text}`)
      .join("\n");
  });
};
