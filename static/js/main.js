/* Phase 0: minimal script proving static JS is served and runs. */

document.addEventListener("DOMContentLoaded", function () {
  var status = document.getElementById("status");
  if (status) {
    status.textContent = "Static JS loaded successfully.";
  }
});
