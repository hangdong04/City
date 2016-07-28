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
	private static final String APP_STATE = "app_state";
	private static final String BUTTON_STATE = "button_state";

	// User value (make variable public to access from outside)
	public static final String KEY_LOCK_SCAN = "lockScan";

	private static final String KEY_Location = "last_location";
	private static final String KEY_APP_STATE = "0";
	private static final String KEY_LABEL = "label";
	private static final String KEY_NUM = "num";
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

	public void saveState(int state){
		editor.putInt(APP_STATE, state);
		editor.commit();
	}

	public int getState(){
		return pref.getInt(APP_STATE ,0);
	}

	public void saveButtonState(int state){
		editor.putInt(BUTTON_STATE,state);
		editor.commit();
	}
	public int getButtonState(){
		return pref.getInt(BUTTON_STATE, 0);
	}

	public void saveLabel(String label) {
		editor.putString(KEY_LABEL, label);
		editor.commit();
	}
	public String getLabel() {
		return pref.getString(KEY_LABEL, "idle");
	}

	public void saveNum(int num){
		editor.putInt(KEY_NUM, num);
		editor.commit();
	}

	public int getNum(){
		return pref.getInt(KEY_NUM, 1);
	}

}
