
def  PID

pipeline {
      
      agent any
 
      
  parameters
  {
    stashedFile 'Archived_File.zip'
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
            steps {
                bat 'echo Unstash Archived_File.zip.'
                unstash 'Archived_File.zip'
                bat  'tar -xf Archived_File.zip'
                bat 'dir'
                
                bat  'unzip_files.bat'
                
                bat 'dir'

                bat 'echo UNZIP Completed.'
                

            }
        }
        
        stage('Running Tests')
        {
            steps 
            {
                
             script
                {
                        PID = bat(script: 'python ProcessID.py .\\destination_folder\\eebus-hub-windows-amd64.exe', returnStdout: true).trim()
      
                        echo "${PID}"
                }
                  
            script
                {  
                        // Run the Python script to execute the Go test and generate the JSON file 
                    bat 'python Run_UseCases.py .\\destination_folder\\examples\\Api\\LPC\\LPC3\\LPC3.go' 
     
                }

            }
        }
        
        stage('Generating CSV Report')
        {
            steps 
            {
 
                script
                {
                    // Generating Csv Report
                    bat 'python generate_csv_report.py'
                }
            }
        }   
     
    }
    
    post { 
        always
        {
            archiveArtifacts artifacts: 'test_results.json, test_results.csv', fingerprint: true

        }  
    }   
}
