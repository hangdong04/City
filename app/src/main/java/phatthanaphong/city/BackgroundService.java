package phatthanaphong.city;

import android.app.ActivityManager;
import android.app.Service;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Handler;
import android.os.IBinder;
import android.util.Log;
import android.widget.Toast;

import java.util.List;

import de.greenrobot.event.EventBus;

public class BackgroundService extends Service {
    private static BackgroundService backgroundService;
    private EventBus eventBus = EventBus.getDefault();

    private boolean isRunningBackground = false;
    private MyPreference myPreference;
    public static GPSTracker gps;
    private static int LOCATION_DISTANCE = 20;
    public static boolean escalate = false;

    private boolean gps_enabled = false;
    private boolean network_enabled = false;
    private boolean check_start = false;
    public static boolean check_cancel_process = false;
    private boolean isFirstStartLocation = true;
    private String TAG = "BackgroundService";
    double last_know_lat;
    double last_know_lon;
    private int speedState = 1;
    private int oldSpeedState = 1;
    Handler handler_start_emergency;

    // Related to state app emergency
    public static int mStateAppEmergency = 0;

    // Related to notifications
    public static boolean airplaneOn = false;
    public static boolean bluetoothOff = false;
    public static boolean dataOff = false;
    public static boolean gpsOff = false;

    // Locations database
//    private DBUtil locationdb;


    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate() {
        backgroundService = this;
        Toast.makeText(this, "Service created!", Toast.LENGTH_LONG).show();
        Log.d(TAG, "onCreate: Background Create" );
        gps = new GPSTracker(backgroundService);
//        locationdb = new DBUtil(backgroundService);
        /////// create preference for get user data
        myPreference = new MyPreference(backgroundService);
//        running_background();
    }

    @Override
    public void onDestroy() {
        stop_running_background();
    }

    private void running_background() {
//        if (!isRunningBackground) {
//            isRunningBackground = true;
//
//            NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder(backgroundService)
//                    .setSmallIcon(R.drawable.ic_notification_24x24)
//                    .setColor(getResources().getColor(R.color.revolar_notification_active))
//                    .setContentTitle(getResources().getString(R.string.notification_title_active))
//                    .setContentText(getString(R.string.notification_detail_active))
//                    .setOngoing(true);
//
//            startForeground(Constant.ID_NOTIFICATION, notificationBuilder.build());
//            if (!appState.device.isRegistered()) {
//                NotificationUtil.hideNotification(backgroundService);
//            } else {
//                NotificationUtil.checkIssueStateNotification(backgroundService);
//            }
//
//        }
    }


    private void stop_running_background() {
        if (isRunningBackground) {
            Log.w(getClass().getName(), "isRunningBackground to stop()!");
            isRunningBackground = false;
            stopForeground(true);
        }
    }

    public boolean isForeground(String myPackage) {
        ActivityManager manager = (ActivityManager) getSystemService(ACTIVITY_SERVICE);
        List<ActivityManager.RunningTaskInfo> runningTaskInfo = manager.getRunningTasks(1);
        ComponentName componentInfo = runningTaskInfo.get(0).topActivity;
        return componentInfo.getPackageName().equals(myPackage);
    }

}