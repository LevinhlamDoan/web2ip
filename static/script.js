function identifyIP() {
    // Get user input
    const url = document.getElementById("url").value;
    // Make AJAX request to Flask backend
    $.ajax({
        url: "/identify_ip",
        type: "POST",
        data: { url: url },
        success: function(response) {
            // Update UI with IP address results
            $("#ipResults").html(response.ip_addresses.join("<br>"));
        },
        error: function(error) {
            console.error("Error:", error);
        }
    });
}