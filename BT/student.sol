// SPDX-License-Identifier: MIT
 pragma solidity ^0.8.20;

 contract StudentData {

     struct Student {
         uint rollNo;
         string name;
         uint age;
         uint marks;
     }

     Student[] public students;

     function addStudent(
         uint _rollNo,
         string memory _name,
         uint _age,
         uint _marks
     ) public {
         students.push(
             Student(_rollNo, _name, _age, _marks)
         );
     }

     function getStudent(uint _index)
         public
         view
         returns (uint, string memory, uint, uint)
     {
         Student memory s = students[_index];

         return (s.rollNo, s.name, s.age, s.marks);
     }

     function getStudentCount() public view returns (uint) {
         return students.length;
     }
 }