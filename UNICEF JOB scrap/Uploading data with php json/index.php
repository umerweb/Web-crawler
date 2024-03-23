<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Job Listings</title>
</head>
<body>
<h1>Job Listings</h1>

<?php
// Read JSON file
$jsonString = file_get_contents('job_listings.json');
$jobListings = json_decode($jsonString, true);

// Loop through job listings
foreach ($jobListings as $job) {
    // Access job data using keys
    $jobTitle = $job['Job-Title'];
    $description = $job['Description'];
    $jobLocation = $job['Job-Location'];
    $jobDeadline = $job['Job-Deadline'];
    $jobLink = $job['Job-a'];

    // Display job data
    echo '<a href="' . $jobLink . '" class="job-link">';
    echo '<div class="job-container">';
    echo '<strong>' . $jobTitle . '</strong><br>';
    echo 'Description: ' . $description . '<br>';
    echo 'Location: ' . $jobLocation . '<br>';
    echo 'Deadline: ' . $jobDeadline . '<br>';
    echo '</div>';
    echo '</a><br>';
}
?>

</body>
</html>
