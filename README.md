# What was this for
This is the prototype repository I used for testing the continous integration workflow for the TensorFlow research team at Purdue University (CAM2)\
The workflow goes as follows:
1. Github actions sets up Google Cloud SDK
2. Github actions spins up a new instance of Google Cloud VM
3. Clone the CAM2 TensorFlow repository into the Google Cloud VM and navigate to correct directory
4. Run unit tests
5. Stop the Google Cloud VM instance
