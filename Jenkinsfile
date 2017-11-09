#!groovy

node {
	stage ('Build') {
		checkout scm
		docker.build('alan/blahapp')
	}
	stage ('Test') {
		docker.image('alan/blahapp').inside('-u root') {
			stage ('Setup tests') {
				sh 'pwd'
				sh 'python --version'
				sh 'python manage.py migrate'
				sh 'python manage.py loaddata blahapp'
			}
			stage ('Run tests') {
				sh 'coverage run manage.py test blahapp -v 2'
				sh 'coverage html'
			}
			stage ('Archive results') {
				archive (includes: 'htmlcov/*')
			}
		}
	}
	stage ('QA') {
		sh 'echo "$BLAHAPP_PROD_SETTINGS"'
		sh 'echo "${env.BRANCH_NAME}"'
	}
}


