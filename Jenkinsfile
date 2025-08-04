pipeline {
    agent any

    tools {
        // Optional: Ensure Git is defined under Manage Jenkins > Global Tools
        git 'Default'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Bhagyavan8050/AttendanceTracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t attendance-tracker-app .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test API') {
    steps {
        script {
            bat '''
                echo Waiting for app to start...
                set RESPONSE=
                for /L %%x in (1,1,30) do (
                    curl -f http://localhost:5000/attendance && set RESPONSE=OK
                    if defined RESPONSE exit /b 0
                    ping -n 2 127.0.0.1 > nul
                )
                echo Application did not respond in time
                exit /b 1
            '''
        }
    }

}


        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhost299', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        bat '''
                            echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                            docker tag attendance-tracker-app %DOCKER_USERNAME%/attendance-tracker-app:latest
                            docker push %DOCKER_USERNAME%/attendance-tracker-app:latest
                        '''
                    }
                }
            }
        }
    }
}
