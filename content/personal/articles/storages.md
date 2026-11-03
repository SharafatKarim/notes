---
title: Storages and Storage Drivers
tags:
- personal
- quick-notes
aliases:
- Storages and Storage Drivers
---

# Storages and Storage Drivers

storage কি? হয়তো হবে কিছু একটা যেটা আমাদের তথ্য রাখে। 

এখন প্রশ্নটা হলো প্রকারভেদ নিয়ে।
storage দুই প্রকার, 

- primary (বেশী পরিমানে read write হয়। অর্থাৎ সবসময় CPU এর সাথে যোগাযোগ active)
- আর secondary storage (সবসময় read, write করার প্রয়োজন নেই)

> ভাবছি ইন্টারনেটে তো না জানি কতো website কতো ভাবে classify করা হয়েছে। যাহোক এ নিয়ে আমার মাথাব্যাথা নেই। আমি একটা সাধারণ ভাবে লেখছি।

| ধরণ | উদাহারণ |
| --- | --- |
| primary | RAM, ROM, cache, register |
| secondary | HDD, SSD, optical, cloud, hybrid |

---

## Primary Storage

[1] RAM = random access memory। volatile = ভুলে যায়। ডেটা ইচ্ছামতো read/ write করা যায়। তবে যদি পিসি বন্ধ হয়ে যায়, সব ডেটা হারিয়ে যায়।

[2] ROM = read only memory। যারা মনে করছেন যে ROM আর SSD এবং HDD কখনোই এক না, android আর iphone এ একটু কাহিনী আছে যার কারণে সবাই এক জিনিষ মনে করে। একটু বিস্তারিত লিখছি,

ROM হলো non-volatile, অর্থাৎ ভুলবে না। পিসি বন্ধ হয়ে গেলেও ডেটা অক্ষুন্ন থাকবে। এর ভিতরে মূলত BIOS/ UEFI firmware থাকে। এর ভেতরে boot loader এবং init system এর লোকেশন লেখা থাকে। যেমন হার্ড ডিস্কের কোন জায়গায় আমাদের operating system টা আছে। এটা দুটো অপারেশন চালায়,

- ram, CPU, GPU সব ঠিকমতো আছে কিনা সেটা প্রথমে পরীক্ষা করে
- দ্বিতীয়ত OS load করে

আগেরকার system এ 4 KB থেকে 1 MB এর মতো থাকতো। বর্তমানে 16-32 MB এর মতো হয় সাইজ।

> android এর ক্ষেত্রে java VM (JVM) এর /mnt ব্যতীত বাকি সব path এর ডেটা কখনোই পরিবর্তন হয় না। তাই আমরা মোবাইলের দোকানে storage বলতে ROM কে ব্যবহার করতে দেখি, কিন্তু ROM কখনোই storage না।

[3] register = CPU এর ভেতর থাকে। এই অংশ পুরোটাই CPU নিয়ন্ত্রণ করে। একসময় c program দিয়ে এটা মোডিফাই করা যেতো, কিন্তু এখন যায় না। এই অংশটা RAM এর চাইতে বহুগুণে fast কারণ এর অবস্থান CPU এর ভেতরে। সাধারণত 6 MB এর আশেপাশে cache memory থাকে আমাদের laptop গুলোতে।

processor এর যেসব ডেটা প্রতিনিয়ত দরকার হয়, এসব তথ্য এখানে রাখা হয়। তারপর তাপমাত্রার sensor এর ব্যাপারগুলো এখানে নিয়ন্ত্রণ করা হয়।

[4] cache = CPU এর পাশেই মাদারবোর্ড এ থাকে। অনেকটা RAM আর CPU এর bridge এর মতো কাজ করে। এটার আকার registor থেকে কিছুটা বেশী ডেটা রাখতে পারে।

---

## Secondary Storage

[1] SSD = solid state drive। হার্ডডিস্কের মতোই, কিন্তু অনেক বেশী fast। এটা একটা chip এর মধ্যে অনেকগুলো memory card বসিয়ে তৈরি করা হয়  মূলত এই কারণে এতো বেশী গতি। গতি 500-3500 MBps। এখন মনে হয় আরো বেশী। গুগল করে দেখুন একটু।

[2] HHD = hard disk drive. এটা SSD এর আগের জেনারেশন। এখানে তথ্য রাখা হয় elelctromegnatic একটা plate এর মতো register দিয়ে। youtube এ simulation video পাবেন। চাইলে দেখতে পারেন। গতি 100-400 MBPS হয়থো। আমার আগের potato পিসিতে 123 mbps ছিলো যতদূর মনে পড়ে।

[3] optical = CD/ DVD। এই আমলে চল নেই, যদিও ছোটবেলায় ব্যবহার করছি অনেক 😅।
[4] cloud = SAAS লিখে গুগল করেন। খুব সুন্দর একটা উদাহারণ google drive, telegram
[5] hybrid = যখন SSD/ HDD একসাথে ব্যবহার করা হয়

> আরো কনফিউসন থাকলে একটু গুগল করে দেখুন, বা জিজ্ঞাসা করুন। কেননা সব আমি কভার করি নি।
