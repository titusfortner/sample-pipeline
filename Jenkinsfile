pipeline {
    agent any

    stages {
        stage('Run Static Code Analysis') {
            steps {
                flake8 .
            }
        }
        stage('Run Unit Tests') {
            steps {
                pytest test_unit.py
            }
        }
        stage('Deploy Application') {
            steps {
            	echo 'TBD'
            }
        }
        stage('Run Functional Tests') {
            steps {
                pytest test_functional.py
            }
        }
    }
}