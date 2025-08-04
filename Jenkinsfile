pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/devops2613/attendancetarcker.git'
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
                '''pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/devops2613/attendancetarcker.git'
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
                bat '''
                    @echo off
                    setlocal enabledelayedexpansion
                    set counter=0

                    :loop
                    set /a counter+=1
                    echo Attempt !counter!...

                    curl -sf http://localhost:5000/health >nul 2>&1
                    if !errorlevel! EQU 0 (
                        echo App is up!
                        exit /b 0
                    )

                    if !counter! GEQ 30 (
                        echo Application did not respond in time.
                        exit /b 1
                    )

                    timeout /t 3 >nul
                    goto loop
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '1234', // Ensure this exists in Jenkins Credentials
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat '''
                        @echo off
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
        }

        stage('Test API') {
            steps {
                script {
                    bat '''
                        echo Waiting for app to start...
                        setlocal enabledelayedexpansion
                        set "counter=0"

                        :loop
                        set /a counter+=1
                        echo Attempt !counter!...                        

                        curl -sf http://localhost:5000/health >nul 2>&1
                        if !errorlevel! EQU 0 (
                            echo App is up!
                            exit /b 0
                        )

                        if !counter! GEQ 30 (
                            echo Application did not respond in time.
                            exit /b 1
                        )

                        ping -n 3 127.0.0.1 >nul
                        goto loop
                    '''
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '1234', // Set this ID in Jenkins > Credentials
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
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
