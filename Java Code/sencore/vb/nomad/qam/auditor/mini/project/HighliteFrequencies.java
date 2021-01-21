// *****************************************************************************
// HighliteFrequencies.java
// Copyright 2019 Sencore, Inc. All rights reserved.
// *****************************************************************************
package sencore.vb.nomad.qam.auditor.mini.project;


import java.awt.Color;
import javax.swing.text.DefaultHighlighter;
import javax.swing.text.Document;
import javax.swing.text.Highlighter;
import javax.swing.text.JTextComponent;

public class HighliteFrequencies {

    class MyHighlightPainter extends DefaultHighlighter.DefaultHighlightPainter {

        public MyHighlightPainter(Color color) {
           super(color);
        }

    }

    Highlighter.HighlightPainter myHighlightPainter = new MyHighlightPainter(Color.red);

    public void RemoveHighlights(JTextComponent textComp) {

       Highlighter hilite = textComp.getHighlighter();
       Highlighter.Highlight[] hilites = hilite.getHighlights();

       for (int i = 0; i < hilites.length; i++) {

          if (hilites[i].getPainter() instanceof MyHighlightPainter) {
             hilite.removeHighlight(hilites[i]);
          }//end of if

       }//end of for
    }

    public void Highlight(JTextComponent textComp, String pattern) {

       RemoveHighlights(textComp);

       try {
          Highlighter hilite = textComp.getHighlighter();
          Document doc = textComp.getDocument();
          String text = doc.getText(0, doc.getLength());
          int pos = 0;

          //Change it to while if you need to highlight multiple patterns
          if ((pos = text.toUpperCase().indexOf(pattern.toUpperCase(), pos)) >= 0) {
             hilite.addHighlight(pos, pos + pattern.length(), myHighlightPainter);
             pos += pattern.length();
          }

       } catch (Exception ex) {
          System.out.println(ex);
       }//end of catch

    }//end of function

}//end of the class
