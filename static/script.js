function toggleCard(contentId) {
    const content = document.getElementById(contentId);
    if (content.classList.contains("open")) {
        // 如果内容已经展开，则折叠
        content.classList.remove("open");
    } else {
        // 如果内容未展开，则展开
        content.classList.add("open");
    }
}