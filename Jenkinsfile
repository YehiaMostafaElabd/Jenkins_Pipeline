
def  PID

pipeline {
      
  agent 
  {
        label "${Agent}"
  }
 
      
  parameters
  {
        string defaultValue: '8080', description: 'If You Are Running Jenkins at Port 8080 Please Select another Port', name: 'PORT'
        stashedFile 'Archived_File.zip'
        string defaultValue: 'built-in', description: 'If you are using another agent please Specify', name: 'Agent'
        string defaultValue: 'python3', description: 'Python Version', name: 'python'
  }
  
  
  stages {
        
        stage('Clean Workspace')
        {
            steps
            {
                script
                {
                 
                    dir ("${WORKSPACE}")
                    {
                          cleanWs()
                          checkout scm
                    }
                }                 

            }
        }
      stage('Unstash and Unzip')
      {
            steps 
              {
               script
               {
                      echo "The Node Used To Run This Build Is ${Agent}"
                      echo "The Port Ruuning EEBUS TOOL is ${PORT}"
               }
                    
                echo "Unstash Archived_File.zip."
                unstash 'Archived_File.zip'
                bat  'tar -xf Archived_File.zip'
                bat 'dir'
                
                bat  'unzip_files.bat'
                
                bat 'dir'

                echo "UNZIP Completed."
            }
      }
      stage('Moving Scripts')
      {
            steps 
            {
                script
                {
                    echo "Clonning eebus-go to destination_folder"
                    bat 'MOVE Run_UseCases.py .\\destination_folder'
                    bat 'MOVE ProcessID.py .\\destination_folder'
                    bat 'MOVE generate_csv_report.py .\\destination_folder'

                    dir ("${WORKSPACE}\\destination_folder")
                    {
                        bat 'mkdir .\\devices\\eebus-go'
                        bat "git clone https://github.com/enbility/eebus-go.git .\\devices\\eebus-go"
                    }
                }
                

            }
      }
        
        stage('Running Tests')
        {
            steps 
            {
             script
                {
                    dir ("${WORKSPACE}\\destination_folder")
                    {
                        PID = bat(script: "${python} ProcessID.py .\\eebus-hub-windows-amd64.exe ${PORT}", returnStdout: true).trim()
                        echo "${PID}"
                                          
                      // Run the Python script to execute the Go test and generate the JSON file 
                        bat "${python} Run_UseCases.py .\\examples\\Api\\LPC\\LPC3\\LPC3.go ${PORT}"
                    }
                }
            }
        }
        
        stage('Generating CSV Report')
        {
            steps 
            {
 
                script
                {
                     dir ("${WORKSPACE}\\destination_folder")
                    {
                        // Generating CSV Report
                        bat "${python} generate_csv_report.py"
                    }
                }
            }
        }   
     
    }
    
    post { 
        always
        {
            dir ("${WORKSPACE}\\destination_folder")
            {
                archiveArtifacts artifacts: 'test_results.json, test_results.csv', fingerprint: true
            }
        }  
    }   
}
