# Using Puppet, create a file in /tmp.
file { '0-create_a_file.pp':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
