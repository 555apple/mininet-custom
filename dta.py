"""Custom topology example

Two directly connected switches plus a host for each switch:

   hosta --- hostd --- hostc
               .
	       .
             hostb
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
 	host4 = self.addHost( 'h4' )
       
        # Add links
        self.addLink( host1, host4 )
        self.addLink( host2, host4)
	self.addLink( host3, host4)
      


topos = { 'mytopo': ( lambda: MyTopo() ) }
