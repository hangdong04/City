package phatthanaphong.city;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;

import java.util.Date;

public class MyPreference {

	SharedPreferences pref;
	SharedPreferences.Editor editor;

	// Shared pref mode
	int PRIVATE_MODE = 0;

	// Sharedpref file name
	private static final String PREF_NAME = "Revolar";


	// User value (make variable public to access from outside)
	public static final String KEY_LOCK_SCAN = "lockScan";

	private static final String KEY_Location = "last_location";
	private static final String KEY_APP_STATE = "0";
	private static final String KEY_LABEL = "label";
	private static final String KEY_BATTERY_LEVEL = "battery_level";
	private static final String KEY_LAST_TIME_CONNECTED = "last_time_connected";
	private static final String KEY_ALERT_ID = "alert_id";
	private static final String KEY_ALERT_LEVEL = "alert_level";
	private static final String KEY_ALERT_RECEIVED_BY_PHONE = "alertReceivedByPhoneAt";
	private static final String KEY_ALERT_SEND_TO_API = "alertSentToApiAt";
	private static final String KEY_ALERT_BUTTON_PRESSED = "buttonPressedAt";

	public MyPreference(Activity activity) {
		pref = activity.getSharedPreferences(PREF_NAME, PRIVATE_MODE);
		editor = pref.edit();
	}

	public MyPreference(Context context) {
		pref = context.getSharedPreferences(PREF_NAME, PRIVATE_MODE);
		editor = pref.edit();
	}

	public void lockScan(boolean lock) {
		editor.putBoolean(KEY_LOCK_SCAN, lock);
		editor.commit();
	}

	public boolean isLockScan() {
		return pref.getBoolean(KEY_LOCK_SCAN, false);
	}

	public void updateAppState(int state) {
		editor.putInt(KEY_APP_STATE, state);
		editor.commit();
	}
	public void saveLabel(String label) {
		editor.putString(KEY_LABEL, label);
		editor.commit();
	}
	public String getLabel() {
		return pref.getString(KEY_LABEL, "idle");
	}
	public void createAlertID(String alert_id) {
		editor.putString(KEY_ALERT_ID, alert_id);
		editor.commit();
	}

	public String getAlertID() {
		return pref.getString(KEY_ALERT_ID, "none");
	}

	public void createAlertLevel(String alert_type) {
		editor.putString(KEY_ALERT_LEVEL, alert_type);
		editor.commit();
	}

	public String getAlertLevel() {
		return pref.getString(KEY_ALERT_LEVEL, "");
	}

	public void createAlertReceived(Date alert_receive) {
		editor.putLong(KEY_ALERT_RECEIVED_BY_PHONE, alert_receive.getTime());
		editor.commit();
	}

	public Date getAlertReceived() {
		return new Date(pref.getLong(KEY_ALERT_RECEIVED_BY_PHONE, 0));
	}

	public void createAlertSendToApi(Date alert_send_to_api) {
		editor.putLong(KEY_ALERT_SEND_TO_API, alert_send_to_api.getTime());
		editor.commit();
	}

	public void createAlertButtonPressed(Date alert_button_pressed) {
		editor.putLong(KEY_ALERT_BUTTON_PRESSED, alert_button_pressed.getTime());
		editor.commit();
	}

	public Date getAlertButtonPressed() {
		return new Date(pref.getLong(KEY_ALERT_BUTTON_PRESSED, 0));
	}

	public int getAppState() {
		return pref.getInt(KEY_APP_STATE, 0);
	}

	public void setLastLocation(String location) {
		editor.putString(KEY_Location, location);
		editor.commit();
	}

	public String getLastLocation() {
		return pref.getString(KEY_Location, "0,0");
	}

	public void setBatteryLevel(int batteryLevel) {
		editor.putInt(KEY_BATTERY_LEVEL, batteryLevel);
		editor.commit();
	}

	public int getBatteryLevel() {
		return pref.getInt(KEY_BATTERY_LEVEL, 0);
	}

	public void setLastTimeConnected() {
		Date currentDate = new Date();
		editor.putLong(KEY_LAST_TIME_CONNECTED, currentDate.getTime());
		editor.commit();
	}

	public Date getLastTimeConnected() {
		Long time = pref.getLong(KEY_LAST_TIME_CONNECTED, 0);
		Date lastdate = new Date(time);
		return lastdate;
	}
}
