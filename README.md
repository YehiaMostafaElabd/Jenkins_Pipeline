<div align="center">
    
  # Jenkins Pipeline To Test LPC
  
![Jenkins_logo svg](https://github.com/user-attachments/assets/9536f033-71a1-4cd8-8a67-f9a6e8f31e9c)

  
  </div>
  
  ---
  
  ## 🎯 Overview
  
  CI-CD Example to test Limitation of Power Consumption use case (LPC) in action. For example:
  
  "Applying Active power consumption limit and failsafe consumption power limit on external EVSE."
  
  ## ✨ Pre-Configurations
  
  - **Jenkins**: Tools and Plugins.
  - **Download EEBUS**: Please Go to Link to Download EEBUS-HUB <https://www.coretech-innovations.com/products/eebushub/download>
  
  Note: We are running on Windows Agent
  
  ### Prerequisites
  
  Ensure you have the following installed:
  
  - Make Sure Git and Python are Installed in Tools [ Dashboard > Manage Jenkins > Tools ]
  - Ensure the Following Plugin is Installed [ Git plugin - Workspace Cleanup Plugin ]
  
  ### Installation
  
  1. Go to Jenkins 
  
  - Select New Item
        ![New Item](https://github.com/user-attachments/assets/bdc6ce62-1092-457b-9432-024f717a4cd2)

  - Enter an item name
  - Select Pipeline
  - Press OK
        ![Save](https://github.com/user-attachments/assets/d1a985b5-dc3c-4cc8-a2d9-b811356d534e)


  - Press Pipeline
    ![Select-Pipeline](https://github.com/user-attachments/assets/84a792f6-90c5-4316-9c72-b5aee9faddcc)

  - [Pipeline > Definition > Pipeline script from SCM]
  - [SCM > Select Git]
  - [Repository URL > <https://www.coretech-innovations.com/products/eebushub/download>]
  - [Press Save]
        ![Save](https://github.com/user-attachments/assets/4730b9fa-9219-4e46-b285-3ed4433d66a3)

  

  2. Go Installation :
  
  - Ensure Go is installed on Windows machine <https://go.dev/doc/install>
  - Ensure Python is Installed with [py launcher Feature] <https://www.python.org/downloads/> 

  
  3. Start the development server:

  ## 📘 Usage
  
  - Select Build NOW
        ![Build NOW](https://github.com/user-attachments/assets/31e0f17b-6e3e-440d-b474-1a2eddc06ae7)
  
  - The Pipeline Will Fail for the First Time
 
  - ![Failed1](https://github.com/user-attachments/assets/f28df571-f16d-4292-bdfd-6192aec87777)

  - Refresh The Page Then Select [Build With Parmeter]

      ![Build](https://github.com/user-attachments/assets/a56eaaa8-7e64-40c7-a255-f26d753daa15)

  - Change The PORT if Jenkins is Running on <http://localhost:8080/>
  - Select the Archived File Downloaded from <https://www.coretech-innovations.com/products/eebushub/download>
  - Click Build
        ![Build](https://github.com/user-attachments/assets/753cb34e-fa5b-44cd-841f-82370a028c89)

- Artifact For Test Case Will Appear After The Build Finsihes
         ![Artifact](https://github.com/user-attachments/assets/c3555dce-2cad-458a-833f-24ee94d146a2)


 


