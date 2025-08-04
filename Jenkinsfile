pipeline {
    agent any

    tools {
        git 'Default' // Make sure Git is configured under Manage Jenkins > Global Tool Configuration
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
                bat '''
                    docker-compose down
                    docker-compose up -d
                    docker-compose ps
                '''
            }
        }

        stage('Test API') {
            steps {
                script {
                    bat '''
                        echo Waiting for app to start...

                        for /L %%i in (1,1,30) do (
                            curl -sf http://localhost:5000/health && exit /b 0
                            timeout /T 2 >nul
                        )

                        echo Application did not respond in time.
                        exit /b 1
                    '''
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1234', usernameVariable: 'msdevops2613@gmail.com', passwordVariable: 'Msdevops@2613')]) {
                    script {
                        bat '''
                            echo Logging in to DockerHub...
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
