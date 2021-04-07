# Install nginx listening on port 80, static html = Holberton School, perm redirect 301

package { 'nginx':
  ensure         => 'installed',
  package_source => 'nginx-mainline'
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  ensure  => present,
  content => 'Holberton School'
}

file { 'custom_404.html':
  path    => '/var/www/html/custom_404.html',
  ensure  => present,
  content => "Ceci n'est pas une page"
}

exec { 'sed1':
  path    => '/usr/bin/env:/usr/bin:/usr/sbin:/bin',
  command => 'sed -r -i "/^\s+server_name .+;/a\ \tlocation /redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default'
}