import { TestBed, inject } from '@angular/core/testing';

import { HostService } from './host.service';

describe('HostService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HostService]
    });
  });

  // it('should ...', inject([HostService], (service: HostService) => {
  //   expect(service).toBeTruthy();
  // }));
});
