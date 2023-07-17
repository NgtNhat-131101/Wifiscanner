import { initializeApp } from 'firebase/app';
import { getDatabase, ref, child, get, onChildAdded  } from "firebase/database";
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite';


// Your web app's Firebase configuration
// For Firebase JS SDK v9.1.3 and later, measurementId is optional
const firebaseConfig = {
apiKey: "AIzaSyA1BMgLRSWkHjIQZKtAGzzQz5vGh64nDCQ",
authDomain: "wifiscanner-a0843.firebaseapp.com",
databaseURL: "https://wifiscanner-a0843-default-rtdb.firebaseio.com",
projectId: "wifiscanner-a0843",
storageBucket: "wifiscanner-a0843.appspot.com",
messagingSenderId: "123196091842",
appId: "1:123196091842:web:2f435bb9bafac1deceba5b",
measurementId: "G-R4D99KH07K"
};

// const dburl = "https://wifiscanner-a0843-default-rtdb.firebaseio.com/NetworkList"
// Initialize Firebase
initializeApp(firebaseConfig);
const database = getDatabase();
const postsRef = ref(database, 'NetworkList');

onChildAdded(postsRef, (value) => {
    const postId = value.key;
    // console.log(typeof postId);
    const postData = value.val();
    // console.log(typeof postData);
    // console.log(postData.lenght);
    // console.log(postData);
    postData.forEach(element => {
    console.log("date: ", element.date);
    console.log("time: ", element.time);
    console.log("ssid: ",element.ssid);
    console.log("rssi: ", element.rssi);
    console.log("frequency: ",element.freq);
    console.log("bssid: ", element.bssid);

      
    });

  });