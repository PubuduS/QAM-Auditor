// *****************************************************************************
// Countdown.java
// Copyright 2019 Sencore, Inc. All rights reserved.
// *****************************************************************************
package sencore.vb.nomad.qam.auditor.mini.project;

import java.util.Timer;
import java.util.TimerTask;
import javax.swing.JLabel;

//This is a countdown m_timer which indicate remainning time to tune channels
public class Countdown {

    //Make both static and also the function SetInterval if runs into problem.
    private int m_interval;
    private Timer m_timer;

    public void CountdownTimer(String secs, JLabel countdown) {

        int delay = 1000;
        int period = 1000;
        m_timer = new Timer();
        m_interval = Integer.parseInt(secs);

        m_timer.scheduleAtFixedRate(new TimerTask() {

            public void run() {

                int seconds = SetInterval();
                int min = seconds / 60; //get minutes
                int sec = seconds % 60; //get seconds
                countdown.setText("Time Remaining: " + min + " Minutes " + sec + " Seconds");

            }
        }, delay, period);

    }

    //Called from cancel button
    public void CancelTimer() {
        m_timer.cancel(); //cancel m_timer by calling this method. otherwise m_timer will run until finished or infinitely.
    }

    private final int SetInterval() {
        if (m_interval == 1) {
            m_timer.cancel();
        }
        return --m_interval;
    }

}//end of the class
