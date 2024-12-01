package com.example.hw1_simpleapp;

import android.util.Log;
import android.util.Pair;

import java.util.Random;
import java.util.Arrays;
import java.util.Vector;

public class Game {
    private int mScore, mBest;
    int[][] mBoard;
    Random mRandom;

    Game() {
        mScore = 0;
        mBest = 0;
        mBoard = new int[4][4];
        mRandom = new Random();
        clearBoard();
    }

    public void clearBoard() {
        for (int[] row : mBoard) {
            Arrays.fill(row, 0);
        }
        mScore = 0;
    }

    public int getScore() {
        return mScore;
    }

    public int getBest() {
        return mBest;
    }

    public int getSquare(int i, int j) {
        return mBoard[i][j];
    }

    public int createRandomSquare() {
        Vector<Integer> empties = new Vector<>();
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j) if (mBoard[i][j] == 0)
                empties.add(i*4 + j);
        if (empties.isEmpty()) return -1;
        int index = empties.get(mRandom.nextInt(empties.size()));
        
        mBoard[index/4][index%4] = 2;
        Log.d("[Game]", "New position: " + index);
        return index;
    }

    public void mergeLeft() {
        for(int[] row : mBoard) {
            Vector<Integer> values = new Vector<>();
            int match = 0;
            for(int val : row) if (val > 0) {
                if (val == match) {
                    values.add(2*val);
                    addScore(2*val);
                    match = 0;
                } else {
                    if (match > 0) values.add(match);
                    match = val;
                }
            }
            if (match > 0) values.add(match);
            Arrays.fill(row, 0);
            for(int i = 0; i < values.size(); ++i) {
                row[i] = values.get(i);
            }
        }
    }

    public void mergeRight() {
        rotate180();
        mergeLeft();
        rotate180();
    }

    public void mergeUp() {
        rotate270();
        mergeLeft();
        rotate90();
    }

    public void mergeDown() {
        rotate90();
        mergeLeft();
        rotate270();
    }

    private void rotate180() {
        int[][] temp = new int[4][4];
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                temp[i][j] = mBoard[3 - i][3 - j];

        for(int i = 0; i < 4; ++i)
            mBoard[i] = Arrays.copyOf(temp[i], temp[i].length);
    }

    private void rotate270() {
        int[][] temp = new int[4][4];
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                temp[i][j] = mBoard[j][3-i];

        for(int i = 0; i < 4; ++i)
            mBoard[i] = Arrays.copyOf(temp[i], temp[i].length);
    }

    private void rotate90() {
        int[][] temp = new int[4][4];
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                temp[i][j] = mBoard[3-j][i];

        for(int i = 0; i < 4; ++i)
            mBoard[i] = Arrays.copyOf(temp[i], temp[i].length);
    }

    private void addScore(int score) {
        mScore += score;
        mBest = Math.max(mBest, mScore);
    }
}
