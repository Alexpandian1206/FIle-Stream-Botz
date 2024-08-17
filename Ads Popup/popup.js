document.addEventListener("DOMContentLoaded", function() {
    const popup = document.getElementById("ad-popup");

    // Set a timer to close the popup after 5 seconds
    setTimeout(function() {
        popup.classList.add("hide");
    }, 5000);  // 5000ms = 5 seconds
});
