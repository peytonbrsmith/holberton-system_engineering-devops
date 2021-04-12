#!/usr/bin/puppet
# configures nginx

package { 'nginx':
  ensure => installed,
}

exec { 'newheader':
  command => 'sed -r -i "/^\s+server_name .+;/a\ \\tadd_header X-Served-By \$HOSTNAME\;\n" /etc/nginx/sites-available/default'
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
