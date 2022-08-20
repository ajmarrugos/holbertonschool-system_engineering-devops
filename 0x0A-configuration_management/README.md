## Configuration management Project

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ" title="Intro to Configuration Management" target="_blank">Intro to Configuration Management</a> </li>
<li><a href="/rltoken/D0-IO_SIZSXYLKJs2BitYA" title="Puppet resource type: file" target="_blank">Puppet resource type: file</a> (<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
<li><a href="/rltoken/Fqmb5rnChQgYAypvKoTxAQ" title="Puppet&#39;s Declarative Language: Modeling Instead of Scripting" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
<li><a href="/rltoken/oezu0m_hJ8nEVA6a9o17Tw" title="Puppet lint" target="_blank">Puppet lint</a> </li>
<li><a href="/rltoken/N70cVw8mG3707He-OxjP1w" title="Puppet emacs mode" target="_blank">Puppet emacs mode</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass <code>puppet-lint</code> version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension <code>.pp</code> </li>
</ul>

<h2>Note on Versioning</h2>

<p>Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled. </p>

<h3>Install <code>puppet</code></h3>

<pre><code>$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
</code></pre>

<p>You do <strong>not</strong> need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet. </p>

<p><a href="/rltoken/_xOod_Lzz8WKTbhpG5SWLQ" title="Puppet 5 Docs" target="_blank">Puppet 5 Docs</a></p>

<h3>Install <code>puppet-lint</code></h3>

<pre><code>$ gem install puppet-lint
</code></pre>

</div>