# automate the task of creating a custom HTTP header response, but with Puppet

exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By 1fd3c92e525b;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
