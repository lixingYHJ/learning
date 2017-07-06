package service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import static org.apache.coyote.http11.Constants.a;

/**
 * Created by lixing on 2017/6/24.
 */
@RestController
public class ConsumerController {
    @Autowired
    ComputeClient computeClient;
    @RequestMapping(value = "/add", method = RequestMethod.GET)
    public String add(@RequestParam Integer a, @RequestParam Integer b) {
        return computeClient.add(a, b);
    }
}
