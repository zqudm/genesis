package genesis.diff;
//import ch.uzh.ifi.seal.changedistiller.*;
//import ch.uzh.ifi.seal.changedistiller.ChangeDistiller;
//import ch.uzh.ifi.seal.changedistiller.model.entities.SourceCodeChange;
import java.io.File;
import java.util.List;
//import ch.uzh.ifi.seal.changedistiller.distilling.FileDistiller;
//import ch.uzh.ifi.seal.changedistiller.ChangeDistiller.Language;
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {

File left = new File("/root/Workspace/genesis-0.21/python/__tmp/src1/tool/src/org/antlr/v4/automata/TailEpsilonRemover.java");
File right = new File("/root/Workspace/genesis-0.21/python/__tmp/src2/tool/src/org/antlr/v4/automata/TailEpsilonRemover.java");
//FileDistiller distiller = ChangeDistiller.createFileDistiller(Language.JAVA);
try {
  //        distiller.extractClassifiedSourceCodeChanges(left, right);
	    //
	    //
} catch(Exception e) {
	    /* An exception most likely indicates a bug in ChangeDistiller. Please file a
	     *        bug report at https://bitbucket.org/sealuzh/tools-changedistiller/issues and
	     *               attach the full stack trace along with the two files that you tried to distill. */
	    System.err.println("Warning: error while change distilling. " + e.getMessage());
}
    }


		     }





