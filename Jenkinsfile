
def  PID

pipeline {
      
      agent any
 
      
  parameters
  {
    stashedFile 'Archived_File.zip'
  }
  
  
  stages {

        
        
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
                        PID = bat(script: 'py ProcessID.py .\\destination_folder\\eebus-hub-windows-amd64.exe', returnStdout: true).trim()
      
                        echo "${PID}"
                }
                  
            script
                {  
                        // Run the Python script to execute the Go test and generate the JSON file 
                    bat 'py Run_UseCases.py .\\destination_folder\\examples\\Api\\LPC\\LPC3\\LPC3.go' 
     
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
                    bat 'py generate_csv_report.py'
                }
            }
        }   
     
    }
    
    post { 
        always
        {
           

            script
            {
                 dir ("${WORKSPACE}")
                {
                  cleanWs(deleteDirs: true,
                          patterns: [[pattern: 'destination_folder', type: 'EXCLUDE'],
                          [pattern: 'logs', type: 'EXCLUDE']])
                   bat  "echo Clean Jenkins Workspace before the build starts"   
                }                  
                    

                    
            }
    
        
        }  
    }   
}
