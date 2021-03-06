from game.nodes.attributes import Connection as GameConnection
from game.nodes.attributes import NodePathTargetConnection as GameNodePathTargetConnection
from game.nodes.attributes import ConnectionList as GameConnectionList
from game.nodes.attributes import NodePathSourceConnectionList as GameNodePathSourceConnectionList
from game.nodes.attributes import NodePathTargetConnectionList as GameNodePathTargetConnectionList


class RegisterMixin( object ):
    
    def Set( self, tgtComp ):
        base.scene.ClearConnections( self.srcComp )
        
        super( RegisterMixin, self ).Set( tgtComp )
    
    def Connect( self, tgtComp ):
        super( RegisterMixin, self ).Connect( tgtComp )
        
        base.scene.RegisterConnection( tgtComp, self )
        
    def Break( self, tgtComp ):
        super( RegisterMixin, self ).Break( tgtComp )
        
        base.scene.DeregisterConnection( tgtComp, self )
        

class Connection( RegisterMixin, GameConnection ): pass
class NodePathTargetConnection( RegisterMixin, GameNodePathTargetConnection ): pass
class ConnectionList( RegisterMixin, GameConnectionList ): pass
class NodePathSourceConnectionList( RegisterMixin, GameNodePathSourceConnectionList ): pass
class NodePathTargetConnectionList( RegisterMixin, GameNodePathTargetConnectionList ): pass