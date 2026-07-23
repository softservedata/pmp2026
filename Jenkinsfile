pipeline {
    agent any
    stages {
         stage('Start') {
            steps {
                echo 'Hello, Start'
            }
        }
        stage('Clone') {
            steps {
                git url: 'https://github.com/softservedata/pmp2026.git', branch: 'contact'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn -B package -DskipTests'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'mvn -B test'
            }
        }
        stage('done') {
            steps {
                echo 'finish'
            }
        }
    }
}

