package com.example.hw1_simpleapp;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.Typeface;
import android.net.Uri;
import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.GestureDetectorCompat;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import android.util.Log;
import android.view.GestureDetector;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.GridLayout;
import android.widget.TextView;

import java.util.Vector;

public class MainActivity extends AppCompatActivity {

    private Game mGame;
    private static int MAX_COLOR = Color.rgb(159, 50, 0); // orange
    private static int START_COLOR = Color.argb(32, 238, 228, 218); // low
    GridLayout mBoard;
    private GestureDetectorCompat detector;
    OnSwipeListener onSwipeListener;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        mGame = new Game();
        initBoardDisplay();
        OnSwipeListener onSwipeListener = new OnSwipeListener() {
            @Override
            public boolean onSwipe(Direction direction) {
                switch (direction) {
                    case up:
                        Log.d("Swipe", "Up");
                        mGame.mergeUp();
                        break;
                    case down:
                        Log.d("Swipe", "Down");
                        mGame.mergeDown();
                        break;
                    case left:
                        Log.d("Swipe", "Left");
                        mGame.mergeLeft();
                        break;
                    case right:
                        Log.d("Swipe", "Right");
                        mGame.mergeRight();
                        break;
                }
                setTextById(R.id.score_box, mGame.getScore());
                setTextById(R.id.best_box, mGame.getBest());
                mGame.createRandomSquare();
                for(int i = 0; i < 16; ++i)
                    updateSquare(i);
                return super.onSwipe(direction);
            }
        };

        detector = new GestureDetectorCompat(getApplicationContext(), onSwipeListener);
    }
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        return detector.onTouchEvent(event);
    }

    void updateSquare(int id) {
        TextView square = (TextView)mBoard.getChildAt(id);
        int value = mGame.getSquare(id/4, id%4);
        int color = getColorByValue(value);

        square.setBackgroundColor(color);
        if (value > 0) {
            square.setText(String.valueOf(value));
        } else {
            square.setText("");
        }
    }

    void createRandomSquare() {
        int id = mGame.createRandomSquare();
        if (id != -1) updateSquare(id);
    }

    public void startNewGame(View view) {
        initBoardDisplay();
    }

    void initBoardDisplay() {
        mGame.clearBoard();
        setTextById(R.id.score_box, mGame.getScore());
        setTextById(R.id.best_box, mGame.getBest());
        drawBoardSquares();
        createRandomSquare();
    }

    void setTextById(int id, int value) {
        TextView textView = findViewById(id);
        textView.setText(String.valueOf(value));
    }

    void drawBoardSquares() {
        mBoard = findViewById(R.id.board);
        mBoard.removeAllViews();
        int margin = 10;

        for(int row = 0; row < 4; ++row) {
            for(int col = 0; col < 4; ++col) {
                TextView square = new TextView(this);
                square.setGravity(Gravity.CENTER);
                square.getAutoSizeMaxTextSize();
                square.setTypeface(square.getTypeface(), Typeface.BOLD);

                GridLayout.LayoutParams params = new GridLayout.LayoutParams();
                params.width = dpToPx(65);
                params.height = dpToPx(65);
                params.setMargins(margin, margin, margin, margin);

                mBoard.addView(square, params);
//                System.out.println(row + " " + col + " " + color)
            }
        }

        for(int id = 0; id < 16; ++id)
            updateSquare(id);
    }

    int getColorByValue(int value) {
        if (value == 0) return START_COLOR;
        double ratio = (Math.min(Math.log(value + 1), 11.0) / 11.0);
        int r = 200;
        int g = (int)(200 * (1-ratio*0.7));
        int b = (int)(200 * (1-ratio));
        return Color.rgb(r, g, b);
    }

    public void onClickWebURL(View view) {
        String url = ((Button)view).getText().toString();
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://" + url));
        startActivity(intent);
    }

    public void onClickTelephone(View view) {
        String number = ((Button)view).getText().toString();
        Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + number));
        startActivity(intent);
    }

    public void onClickEmail(View view) {
        String email = ((Button)view).getText().toString();
        Intent intent = new Intent(Intent.ACTION_SENDTO, Uri.parse("mailto:" + email));
        startActivity(intent);
    }

    private int dpToPx(int dp) {
        float density = getResources().getDisplayMetrics().density;
        return Math.round((float) dp * density);
    }

}