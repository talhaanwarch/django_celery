// Log a message to the console for debugging purposes
console.log('Hello from script.js');

// **Form submission:**

// Attach a submit event listener to the form with ID "myForm"
$("#myForm").submit(function(event) {
  // Prevent the default form submission behavior (full page reload)
  event.preventDefault();

  // Serialize the form data into a query string format
  let formData = $(this).serialize();

  // Log the form data to the console for debugging
  console.log("formData",formData);

  // **Submit the form data via AJAX:**

  $.ajax({
    "url": "/",             // Send the request to the home page URL (presumably a server-side view)
    "type": "POST",         // Use the POST method to send data
    "data": formData,       // Include the serialized form data in the request
    "success": function(response) {
      // Log the response from the server to the console
      console.log("submit", response['output_text']);

      // Extract the task ID from the response
      let taskId = response['output_text'];

      // Initiate a periodic check for the task result
      let intervalId = setInterval(function() {
        checkResult(taskId, intervalId);
      }, 2000); // Check every 2 seconds
    },
    "error": function(error) {
      // Handle any errors that occur during the AJAX request
      console.log("error",error);
    }
  });
});

// **Checking the task result:**

function checkResult(taskId, intervalId) {
  console.log('Checking result for task id: ' + taskId);

  // **Make an AJAX request to check the task status:**

  $.ajax({
    "url": "/check_task_result/" + taskId,  // Send the request to a URL that provides task status
    "type": "GET",                          // Use the GET method to retrieve data
    "success": function(response) {
      // Extract the task status and result from the response coming from views.py check_task_result
      let status = response['status'];
      let result = response['output'];

      // Display the result appropriately based on the status
      displayResult(status, result, intervalId);
    },
    "error": function(error) {
      // Handle any errors that occur during the AJAX request
      console.log("Error", error);
    }
  });
}

// **Displaying the task result:**

function displayResult(status, result, intervalId) {
  if (status === 'SUCCESS') {
    // Clear the interval since the task is complete
    clearInterval(intervalId);

    // Display the successful result in an element with ID "output"
    $("#output").text(result);

    // Log the successful result to the console
    console.log('Task is completed', result);
  } else if (status === 'PENDING') {
    // Display a message indicating the task is still running
    $("#output").text("Please wait!!! Task is still running...");

    // Log the pending status to the console
    console.log('Task is still running', status);
  } else {
    // Display an error message indicating task failure
    $("#output").text('Task Failed');

    // Log the failure status to the console
    console.log('Task Failed Error', status);
  }
}