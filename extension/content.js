function getVideoId() {
  const params = new URLSearchParams(window.location.search);
  return params.get("v");
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "GET_VIDEO_ID") {
    sendResponse({ videoId: getVideoId() });
  }
});
