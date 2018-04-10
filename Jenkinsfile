pipeline {
    agent any

    stages {
        stage('Run Static Code Analysis') {
            steps {
                echo 'I made a different code change'
            }
        }
        stage('Run Unit Tests') {
            steps {
                echo 'Passed'
            }
        }
        stage('Deploy Application') {
            steps {
            	echo 'Passed'
            }
        }
        stage('Run Functional Tests') {
            steps {
                echo 'Passed'
            }
        }
    }
}
